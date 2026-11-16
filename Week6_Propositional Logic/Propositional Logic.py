from itertools import product

def implies(a, b):
    return (not a) or b

def evaluate_kb(P, Q, R):
    s1 = implies(Q, P)
    s2 = implies(P, not Q)
    s3 = Q or R
    return s1 and s2 and s3

def tt_entails(query):
    symbols = ["P", "Q", "R"]

    for values in product([False, True], repeat=3):
        model = dict(zip(symbols, values))

        if evaluate_kb(model["P"], model["Q"], model["R"]):
            if not query(model):
                return False

    return True

print("P Q R | Q->P P->~Q Q|R | KB")
print("-" * 35)

for values in product([False, True], repeat=3):
    P, Q, R = values

    s1 = implies(Q, P)
    s2 = implies(P, not Q)
    s3 = Q or R
    kb = s1 and s2 and s3

    print(P, Q, R, "|", s1, s2, s3, "|", kb)

print("\nEntailment Results:")

print("KB entails R:", tt_entails(lambda m: m["R"]))

print("KB entails R -> P:",
      tt_entails(lambda m: implies(m["R"], m["P"])))

print("KB entails Q -> R:",
      tt_entails(lambda m: implies(m["Q"], m["R"])))
