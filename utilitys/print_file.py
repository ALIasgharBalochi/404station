def save_to_file(filename,**kwargs):

    with open(filename,'a') as f:
        item = []
        for k,w in kwargs.items():
            item.append(f"{k}: {w}")
        f.write(",".join(item) + "\n") 
    return True