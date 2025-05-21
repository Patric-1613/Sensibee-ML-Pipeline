from src.dataset_split import load_image_label_pairs, split_dataset, print_summary

if __name__ == "__main__":
    # Change this to match your real dataset path on Drive
    path = "/content/drive/MyDrive/data_5/final_merged_dataset_half"
    output = f"{path}/final_merged_dataset_half_split_git"

    cls_img_dict, bg_imgs = load_image_label_pairs(path)
    split_dataset(path, output, cls_img_dict, bg_imgs)
    print_summary("Half Dataset", cls_img_dict, bg_imgs)
