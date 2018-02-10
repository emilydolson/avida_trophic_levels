import glob
import sys
import pandas as pd


frames = []

for res_dir in glob.glob(sys.argv[1]):
    avg_data = pd.read_csv(res_dir+"/average.dat", delimiter= " ", skiprows=19, header=None, names = ["update","merit", "gestation", "fitness", "repro_rate", "dep_size", "copied_size", "executed_size", "dep_abundance", "prop_birth", "breed_true", "dep_depth", "generation", "neutral", "label", "true_rep_rate"], index_col=False)
    #print(avg_data)
    task_data = pd.read_csv(res_dir+"/tasks.dat", delimiter= " ", header=None, skiprows=15, names=["update","not","nand","and","orn","or","andn","nor","xor","equ"], index_col=False)
    resource_data = pd.read_csv(res_dir+"/resource.dat", delimiter= " ", header=None, skiprows=15, names=["update","resnot", "resnand", "resand", "resorn", "resor", "resandn","resnor","resxor","resequ"], index_col=False)

    task_data = task_data.set_index("update")
    resource_data = resource_data.set_index("update")
    avg_data = avg_data.set_index("update")

    all_data = pd.concat([avg_data, task_data,resource_data],axis=1)
    all_data["seed"] = res_dir.split("/")[-2].split("_")[-1]
    all_data["condition"] = res_dir.split("/")[-2].split("_")[-2]

    frames.append(all_data)

all_data = pd.concat(frames)

all_data.to_csv("all_data.csv")
