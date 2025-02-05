import numpy as np
import matplotlib.pyplot as plt

def naive_grad(x, mu):
    # the naive gradient to mu
    # \nabla_\mu \mathbb{E}_q[x^2] = \mathbb{E}_q[x^2(x-\mu)] (derivated from REINFORCE)
    return np.mean(x ** 2 * (x - mu))

def reparam_grad(eps, mu):
    #### You need to finish the reparameterization gradient to mu here ####
    # let x = \mu + \epsilon, where \epsilon is a standard normal random variable
    # then the reparameterization gradient to mu is:
    # \nabla_\mu \mathbb{E}_q[(\mu + \epsilon)^2]
    # = \mathbb{E}_q[2 * (\mu + \epsilon)]
    return np.mean(2 * (mu + eps))

def main():
    data_size_list = [10, 100, 500, 1000, 5000] 
    sample_num = 100
    mu, sigma = 2.0, 1.0
    # variance of the gradient to mu
    var1 = np.zeros(len(data_size_list))
    var2 = np.zeros(len(data_size_list))
    exp1 = np.zeros(len(data_size_list))
    exp2 = np.zeros(len(data_size_list))
    for i, data_size in enumerate(data_size_list): 
        estimation1 = np.zeros(sample_num) 
        estimation2 = np.zeros(sample_num)
        for n in range(sample_num):
            # 1.naive method
            x = np.random.normal(mu, sigma, size=(data_size, )) 
            estimation1[n] = naive_grad(x, mu)

            # 2.reparameterization method
            eps = np.random.normal(0.0, 1.0, size=(data_size, )) 
            x = eps * sigma + mu
            estimation2[n] = reparam_grad(eps, mu)
        var1[i] = np.var(estimation1) 
        var2[i] = np.var(estimation2)
        exp1[i] = np.mean(estimation1)
        exp2[i] = np.mean(estimation2)

    print('naive grad variance: {}'.format(var1)) 
    print('reparameterization grad variance: {}'.format(var2)) # plot figure
    index = [_ for _ in range(len(data_size_list))] 
    plt.plot(index, var1)
    plt.plot(index, var2)
    plt.plot(index, exp1)
    plt.plot(index, exp2)
    plt.xticks(index, data_size_list)
    plt.legend(['naive_var', 'reparam_var', 'naive_exp', 'reparam_exp']) 
    plt.savefig('reparam.png')
    plt.show()

if __name__ == "__main__": 
    main()