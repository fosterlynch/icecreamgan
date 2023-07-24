import tensorflow as tf 
import numpy as np 
  


# a very vanilla GAN
# TODO: better architecture like RNN GAN
# https://github.com/olofmogren/c-rnn-gan/blob/master/rnn_gan.py

# Generator 
def generator(z, reuse = None): 
    with tf.variable_scope('gen', reuse = reuse): 
        hidden1 = tf.layers.dense(
            inputs=z,
            units=128,
            activation=tf.nn.leaky_relu
        )
        hidden2 = tf.layers.dense(
            inputs=hidden1,
            units=128,
            activation=tf.nn.leaky_relu,
        )
        output = tf.layers.dense(
            inputs=hidden2,
            units=784,
            activation=tf.nn.tanh
        )
          
        return output 
  
# Discriminator  
def discriminator(X, reuse = None): 
    with tf.variable_scope('dis', reuse = reuse): 
        hidden1 = tf.layers.dense(
            inputs=X,
            units=128,
            activation=tf.nn.leaky_relu,
        hidden2 = tf.layers.dense(
            inputs=hidden1,
            units=128,
            activation=tf.nn.leaky_relu,
        )        
        logits = tf.layers.dense(hidden2, units=1) 
        output = tf.sigmoid(logits)
          
        return output, logits 

  
# defining the loss function 
def loss_func(logits_in, labels_in):
    entropy = tf.nn.sigmoid_cross_entropy_with_logits(
        logits=logits_in, labels=labels_in
    )
    return tf.reduce_mean(entropy)