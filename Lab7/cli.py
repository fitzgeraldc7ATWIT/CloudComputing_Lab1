import argparse
from queries import run_query

def main():
    parser = argparse.ArgumentParser(description="Lab 6 Query Runner")
    parser.add_argument("--query", help="Query key to run (q1, q2, ... q10)", required=True)
    args = parser.parse_args()

    try:
        results = run_query(args.query)
        if not results:
            print("No results found.")
        else:
            for row in results:
                print(row)
    except KeyError as e:
        print(e)
    except Exception as e:
        print(f"Error running query: {e}")

if __name__ == "__main__":
    main()