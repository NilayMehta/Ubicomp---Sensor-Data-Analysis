import iosParser
from plot_data import plot_data
import math
import util
import matplotlib.pyplot as plt 


def count_steps(data):
    print "Accelerometer data graph"
    plot_data(data)
    num_steps = 0
    '''
    ADD YOUR CODE HERE. This function counts the number of steps in data and returns the number of steps
    '''
    return num_steps

def plot_mag(data):
    plt.clf()
    plt.title('Magnitude Plot')
    plt.plot(data, label="Magnitude")
    plt.legend(loc='upper right')
    plt.show()


def run():
    # Get data
    file_name = "data.txt"  # Change to your file name
    data = iosParser.get_data(file_name)
    # print data
    number_of_steps = count_steps(data)
    magnitudes = util.vector_magnitude(data)
    plot_mag(magnitudes)
    moving_avg = util.moving_average(magnitudes,10)
    plot_mag(moving_avg)


    print "Number of steps counted are :", number_of_steps

run()

