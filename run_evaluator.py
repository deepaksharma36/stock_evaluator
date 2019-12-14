import yaml
import argparse
from easydict import EasyDict as edict
from dcf import simple_dcf_value

cfg =  edict()

def yfile_to_cfg(file_path):
    with open(file_path) as fp:
        cfg_file = edict(yaml.load(fp))
    return cfg_file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--company_yaml", "-cy")
    args = parser.parse_args()
    dfc_parms = yfile_to_cfg(args.company_yaml)
    value = simple_dcf_value(dfc_parms.ccf, dfc_parms.grow_r, dfc_parms.disct_r,
        dfc_parms.period)
    print("fair_stock_value", value/dfc_parms.volume)


if __name__ == "__main__":
    main()
