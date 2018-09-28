from scipy.signal import butter, lfilter
import numpy
import math

def vector_magnitude(data):
    """ function to calculate the magnitude of a vector

    Calculate the magnitude of the vector superposition of data (for
    example, acceleration) on x, y, and z axis

    Arguments:
        data: array of (x, y, z) tuples for a vector

    Returns:
        array of the magnitude of a vector

    """
    magnitudes = []
    for datapoint in data:
        magnitude = float(datapoint[0]) ** 2 + float(datapoint[1]) ** 2 + float(datapoint[2]) ** 2
        magnitude = math.sqrt(magnitude)
        magnitudes.append(magnitude)
    return magnitudes



def moving_average(data, window_size):
    """ moving average filter

    Implement a simple moving average filter to use as a low pass
    filter

    Arguments:
        data: data be filtered
        window_size: window_size chosen for the data

    Returns:
        The filtered data.

    TODO:
        Finish this function. Think about how you want to handle
        the size difference between your input array and output array.
        You can write it yourself or consider using numpy.convole for
        it:
        https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html

    

    """

    sliding_window = [1/float(window_size)]*window_size

    convolve_data = numpy.convolve(sliding_window, data)

    print sliding_window

    return numpy.array(convolve_data)
    


def butter_lowpass_filter(data, cutoff, fs, order=5):
    """ butter lowpass filter

    See this link for more information:
    https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.butter.html

    Arguments:
        data: data be filtered
        curoff: cutoff freqency of the filter
        fs: sample rate of data
        order: order of the lowpass filter

    Returns:
        The filtered data.

    TODO:
        Figure out the parameter when you call this function

    """
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

