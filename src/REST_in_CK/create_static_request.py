import json
import numpy as np
from scipy.stats import t
import itertools

DEST_DIR = "./src/REST_in_CK/static/requests"
HEAD_GENES = ["gene_jaw_height",
"gene_jaw_width",
"gene_eye_angle",
"gene_eye_height",
"gene_eye_distance"]
KEY_PREFIX = "head_genes"

def create_range(n_buckets, gaussian):
    a, b = 0, 255
    mean, std = (b - a)/2, 64
    
    break_points_uniform = np.linspace(0, 1, n_buckets + 2)[1:-1]
    break_points = t.ppf(break_points_uniform, df=n_buckets-1, loc=mean, scale=std) \
        if gaussian else 2*mean*break_points_uniform
    return np.rint(break_points)


def create_key(i):
    return f"{KEY_PREFIX}_{str(i).zfill(10)}"

def create_values(vals):
    return {gene_name: val for gene_name, val in zip(HEAD_GENES, vals)}


def create_distributed_request(n_buckets):
    gaussian = True
    range = create_range(n_buckets, gaussian)
    n_repeats = len(HEAD_GENES)
    return {create_key(i): create_values(vals) 
            for i, vals in enumerate(itertools.product(range, repeat=n_repeats))}
        
   
def save_to_json(request):
    path = f"{DEST_DIR}/head_genes.json"
    with open(path, "w") as file:
        json.dump(request, file)


def main():
    request = create_distributed_request(10)
    save_to_json(request)

if __name__ == "__main__":
    main()