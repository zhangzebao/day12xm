import yaml
import config


def read_data(filename):
    with open(config.BASE_PATH + "/data/{}".format(filename), "r", encoding="utf-8")as f:
        return yaml.load(f)


if __name__ == '__main__':
    # print(read_data("data.yaml").values())
    # data = []
    # for i in read_data("data.yaml").values():
    #     data.append((i.get("username"),
    #                  i.get("password"),
    #                  i.get("success"),
    #                  i.get("expect")))
    # print(data)
    data1 = []
    data1.append(tuple(read_data("address.yaml").get("add_address").values()))
    print(data1)
