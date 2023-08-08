#!/usr/bin/env python3

import random
from argparse import ArgumentParser
import pandas as pd
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

def get_option():
    argparser=ArgumentParser()
    argparser.add_argument('--init_a', default=1, help='initailize a', type=float)
    argparser.add_argument('--init_b', default=1, help='initialize b', type=float)
    argparser.add_argument('--prob_r', default=0.3, help='probability for r', type=float)
    argparser.add_argument('--data_len', default=150, help='length for data', type=int)
    argparser.add_argument('--save_interval', default=10, help='interval step', type=int)
    argparser.add_argument('--save_dir', default="./pictures", help='save directory')
    return argparser.parse_args()

def get_list_binomial(prob, len):
    weights = [prob, 1-prob]
    binomial_list = random.choices(["red","white"], weights=weights, k=len)
    #df = pd.DataFrame({"" : binomial_list})
    return binomial_list

def vis_mu_distribution(save_dir, step, a, b):
    x = np.linspace(0, 1, 101)
    y = beta.pdf(x, a, b)

    save_name = "{}/{}.png".format(save_dir, step)
    plt.figure(figsize=(8, 4.5), facecolor="w")
    plt.plot(x, y, label = f"{a=}, {b=}")
    plt.legend(loc = "upper right")
    plt.tight_layout()
    plt.savefig(save_name)

def main(args):
    data_list = get_list_binomial(args.prob_r, args.data_len)
    sum_r = 0
    a = args.init_a
    b = args.init_b
    max_step = args.data_len
    save_interval = args.save_interval
    save_dir = args.save_dir
    for step in range(max_step):
        data = data_list[step]
        sum_r = sum_r + 1 if data == "red" else sum_r
        a_hut = sum_r + a
        b_hut = step - sum_r + b
        mu = (sum_r + a)/(step+a+b)
        if (step % save_interval == 0):
            vis_mu_distribution(save_dir, step, a_hut, b_hut)
            print (mu)

if __name__ =="__main__":
    args=get_option()
    main(args)