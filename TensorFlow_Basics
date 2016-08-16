##core graph data structures

#class tf.Graph

A graph contains a set of Operation objects.

Operation objects: units of computation.

Tensor objects: units of data that flow between operations.
 
There is an already registered default graph. you call access it by calling tf.get_default_graph().

c = tf.constant(4.0)
assert c.graph is tf.get_default_graph()
 
#class tf.Operation

An Operation is a node in a TensorFlow Graph that takes zero or more Tensor objects as input, 
and produces zero or more Tensor objects as output.

For example c = tf.matmul(a, b) creates an Operation of type "MatMul" that takes tensors a and b as input, 
and produces c as output.

#class tf.Tensor

A Tensor represents a value produced by an Operation.

ex.Build a dataflow graph.
c = tf.constant([[1.0, 2.0], [3.0, 4.0]])
d = tf.constant([[1.0, 1.0], [0.0, 1.0]])
e = tf.matmul(c, d)

Construct a `Session` to execute the graph.
sess = tf.Session()

Execute the graph and store the value that `e` represents in `result`.
result = sess.run(e)
