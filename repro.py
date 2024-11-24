from polyply.src.gen_coords import gen_coords


def main():
    gen_coords("assets/topology.top",
               "SEBS_10.gro",
               "polymer",
               density=700, # 0.7 g/mL
               )


if __name__ == "__main__":
    main()
