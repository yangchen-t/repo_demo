import sys
import os

# 传入3个参数，具体操作根据个人情况
def main(argv):
    csv_file = sys.argv[1]
    t_1 = sys.argv[2]
    t_2 = sys.argv[3]
    sum_number  = csv_file + t_1 + t_2
    print(sum_number)
if __name__ == "__main__":
    main(sys.argv)