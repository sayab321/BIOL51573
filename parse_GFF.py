import argparse

def main():
    # Initialize the ArgumentParser       
    parser = argparse.ArgumentParser(description="script to parse genome FASTA and GFF files.")

    # Use generic names like 'fasta' and 'gff'
    parser.add_argument("fasta", help="Path to the genome FASTA file")
    parser.add_argument("gff", help="Path to the GFF file")

    # Parse the arguments
    args = parser.parse_args()

    # Access the values using the names defined above
    print(f"Genome FASTA file: {args.fasta}")
    print(f"GFF file: {args.gff}")

if __name__ == "__main__":
    main()
