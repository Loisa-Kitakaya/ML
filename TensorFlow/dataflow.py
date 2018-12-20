import tensorflow as tf

def func_1():

	a = tf.add(3, 5)

	with tf.Session() as sess:

		print (sess.run(a))

def func_2():

	x = 2

	y = 3

	operation_1 = tf.add(x, y)

	operation_2 = tf.multiply(x, y)

	operation_3 = tf.pow(operation_1, operation_2)

	with tf.Session() as sess:

		operation_3 = sess.run(operation_3)

		print (operation_3)

def func_3():

	x = 2

	y = 3

	add_operation = tf.add(x, y)

	multiply_operation = tf.multiply(x, y)

	useless = tf.multiply(x, add_operation)

	power_operation = tf.pow(add_operation, multiply_operation)

	with tf.Session() as sess:

		z = sess.run(power_operation)

		print (z)

def main():

	#func_1()
	#func_2()
	func_3()

if __name__ == "__main__":

	main()