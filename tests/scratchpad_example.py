from data.get_stocks import get_stock_data
from algorithms.naive_star_boat.alg import NaiveStarBoat
from algorithms.bang_bang.alg import BangBang


##################################################################################
# This is just a template file, make your own copy before doing any scratch work #
##################################################################################


def main():
    # This is a list of the class names (uninitialized) of all algorithms
    algorithm_class_list = [NaiveStarBoat, BangBang]

    # Create an instance of each algorithm listed in algorithm_class_list
    algorithm_instance_list = [alg_class()
                               for alg_class in algorithm_class_list]

    data = get_stock_data("MSFT", "max")

    # TODO: Use the logging library as seen in that mCoding video. Set up CLI args

    breakpoint()


if __name__ == "__main__":
    main()