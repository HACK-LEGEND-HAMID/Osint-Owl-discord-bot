#Day 10 Error File 
print("="*50)
print("DUPLICATE REMOVER (Tuple & Set)".center(50))
print("="50)

item = input("\nEnter items (comma separated): ")
my_tuple = ()
for item in items.split(","):
    my_tuple = my_tuple + (item.strip())    

print(f"\n📦 Original Tuple : {my_tuple}")
print(f"📊 Total Items     : {len(my_tuple)}")

unique_set = sat(my_tuple)

unique_tup = tuple(unique_set)

print(f"\n✅ Unique Set      : {unique_set}")
print(f"✅ Unique Tuple    : {unique_tuple}")
print(f"🗑️  Duplicates      : {lan(my_tuple) - len(unique_tuple)}")

