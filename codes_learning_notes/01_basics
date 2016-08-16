##tf.linspace(start,stop,num,name=None)

#This command generats values in an interval.

#ex.
tf.linspace(10.0,12.0,3,name="linspace")

#the output is [10.0 11.0 12.0]
#(name is the name for the operation)

##tf.InteractiveSession()

#A Tensoflow Session for use in interactive contexts, such as a shell.

#The only difference with a regular Session is that an InteractiveSession 
#installs itself as the default session on construction. 
#The methods Tensor.eval() and Operation.run() will use that session to run ops.

#ex.
sess = tf.InteractiveSession()
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b
#We can just use 'c.eval()' without passing 'sess'
print(c.eval())
sess.close()


##c.eval()

##We can draw a Gaussian Distribution with the values from [-3,3].

sigma=1.0
mean=0.0
z = (tf.exp(tf.neg(tf.pow(x - mean, 2.0) /
                   (2.0 * tf.pow(sigma, 2.0)))) *
     (1.0 / (sigma * tf.sqrt(2.0 * 3.1415))))

#By default, new operations are added to the default Graph.
assert z.graph is tf.get_default_graph()

#execute the graph and plot the result
plt.plot(z.eval())



#now we make a 2d gaussian, which is to multiply two 1d gaussian

z_2d = tf.matmul(tf.reshape(z, [n_values, 1]), tf.reshape(z, [1, n_values]))
#z（1*32），【32，1】=【1，1，……，1，1】（1*32）

#execute and show
plt.imshow(z_2d.eval())

##We create a Garbor patch now!

#In image processing, a Gabor filter, named after Dennis Gabor, 
#is a linear filter used for edge detection. 
#Frequency and orientation representations of Gabor filters 
#are similar to those of the human visual system, and they have 
#been found to be particularly appropriate for texture representation
# and discrimination. In the spatial domain, a 2D Gabor filter is a
# Gaussian kernel function modulated by a sinusoidal plane wave.

x = tf.reshape(tf.sin(tf.linspace(-3.0, 3.0, n_values)), [n_values, 1])
y = tf.reshape(tf.ones_like(x), [1, n_values])
z = tf.mul(tf.matmul(x, y), z_2d)
plt.imshow(z.eval())


# Lets try creating a generic function for computing the same thing:
def gabor(n_values=32, sigma=1.0, mean=0.0):
    x = tf.linspace(-3.0, 3.0, n_values)
    z = (tf.exp(tf.neg(tf.pow(x - mean, 2.0) /
                       (2.0 * tf.pow(sigma, 2.0)))) *
         (1.0 / (sigma * tf.sqrt(2.0 * 3.1415))))
    gauss_kernel = tf.matmul(
        tf.reshape(z, [n_values, 1]), tf.reshape(z, [1, n_values]))
    x = tf.reshape(tf.sin(tf.linspace(-3.0, 3.0, n_values)), [n_values, 1])
    y = tf.reshape(tf.ones_like(x), [1, n_values])
    gabor_kernel = tf.mul(tf.matmul(x, y), gauss_kernel)
    return gabor_kernel

plt.imshow(gabor().eval())

#~~~~~~too tired today, convolve part leaves to tomorrow!~~~~~~~~~~~~~~










