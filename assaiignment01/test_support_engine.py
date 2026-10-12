from support_engine import classify_support, format_message


assert classify_support(59.9, 90, 0) == "High priority"
assert classify_support(60, 90, 4) == "High priority"

assert classify_support(74.9, 90, 0) == "Moderate priority"
assert classify_support(75, 59.9, 0) == "Moderate priority"
assert classify_support(90, 90, 2) == "Moderate priority"

assert classify_support(75, 60, 1) == "Routine monitoring"
assert classify_support(100, 100, 0) == "Routine monitoring"

assert (
    format_message("High priority")
    == "Immediate academic support is recommended."
)

assert (
    format_message("Moderate priority")
    == "Monitor progress and provide targeted guidance."
)

assert (
    format_message("Routine monitoring")
    == "Continue routine monitoring."
)


print("All tests passed.")