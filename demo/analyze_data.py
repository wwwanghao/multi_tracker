from optparse import OptionParser
import multi_tracker_analysis as mta
import matplotlib.pyplot as plt


def simple_plot(datafile):
    data = mta.read_csv_file_to_python.load_data_as_python_object_from_csv_file( datafile )
    length = 50
    mta.plot.plot_trajectories(data, length)
    plt.show()


if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("--datafile", type="str", dest="datafile", default='data.csv',
                    help="path to csv data file to analyze, probably data.csv (the default)")
    (options, args) = parser.parse_args()
    
    datafile = options.datafile
    
    simple_plot(datafile)