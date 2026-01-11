# Routing Problem with Multi-Objective Optimization (MOO)

> [!IMPORTANT]\
> This applications runs **Python 3.14.0** (check `.python-version` file).

## Setup

> [!NOTE]\
> Assuming your environment is Linux, the following steps are completely valid.
> However, if it is not, **please refer to the link at the end of the section**.

First, create Python virtual enviroment using the following command:

```bash
python -m venv <env-directory>

# for example, something like...
python -m venv .venv
```

> [!TIP]\
> If you have any questions, please consult:
> [(Python Land) Python venv: How To Create, Activate, Deactivate, And Delete](https://python.land/virtual-environments/virtualenv#google_vignette)

## CVRP/TSPLIB Notation

An adaptation of the **CVRP** notation was used in the input files
(located in `./resources/vrp/*.vrp`) using the following pattern:

```text
dimension;capacity

# nodes
id_0;x_0;y_0 # represents the coordinates of the deposit
id_1;x_1;y_1
id_2;x_2;y_2
# ...
id_k;x_k;y_k

# demand
id_1;d_1
id_2;d_2
#...
id_k;d_k

# which ones are deposits?
id_0;...
```
