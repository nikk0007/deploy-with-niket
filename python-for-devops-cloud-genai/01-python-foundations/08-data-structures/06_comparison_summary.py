# Section 6: QUICK COMPARISON
# A single script that builds each data type and prints a summary,
# useful as an on-screen recap during the video.

s: str = "prod-api-server-01"
l: list = ["server-01", "server-02", "server-03"]
t: tuple = ("prod-db.internal", 5432)
st: set = {"ap-south-1", "us-east-1"}
d: dict = {"hostname": "prod-api-01", "port": 8080}

print("str   ->", s, "| type:", type(s).__name__)
print("list  ->", l, "| type:", type(l).__name__)
print("tuple ->", t, "| type:", type(t).__name__)
print("set   ->", st, "| type:", type(st).__name__)
print("dict  ->", d, "| type:", type(d).__name__)

print()
print(f"{'Type':<6} {'Ordered':<8} {'Mutable':<8} {'Duplicates':<11} Use When")
print(f"{'str':<6} {'YES':<8} {'NO':<8} {'YES':<11} Text data")
print(f"{'list':<6} {'YES':<8} {'YES':<8} {'YES':<11} Ordered growing data")
print(f"{'tuple':<6} {'YES':<8} {'NO':<8} {'YES':<11} Fixed records")
print(f"{'set':<6} {'NO':<8} {'YES':<8} {'NO':<11} Unique values")
print(f"{'dict':<6} {'YES':<8} {'YES':<8} {'Keys:NO':<11} Named fields, JSON")

print()
print("One-line rule:")
print("  Label or text?                -> str")
print("  Order matters and will change? -> list")
print("  Fixed record, never changes?   -> tuple")
print("  Need uniqueness / set math?    -> set")
print("  Named fields (like JSON)?      -> dict")
