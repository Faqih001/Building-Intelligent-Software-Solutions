# Task 1: AI-Powered Code Completion

# AI-Suggested Implementation (e.g., Copilot)
def sort_dicts_by_key(dicts, key):
    """Sort a list of dictionaries by a specific key using built-in sorted."""
    return sorted(dicts, key=lambda x: x[key])

# Manual Implementation
def sort_dicts_by_key_manual(dicts, key):
    """Sort a list of dictionaries by a specific key using manual sorting (bubble sort)."""
    for i in range(len(dicts)):
        for j in range(i + 1, len(dicts)):
            if dicts[i][key] > dicts[j][key]:
                dicts[i], dicts[j] = dicts[j], dicts[i]
    return dicts

if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    print("AI-suggested:", sort_dicts_by_key(data, "age"))
    print("Manual:", sort_dicts_by_key_manual(data.copy(), "age"))

    # Analysis
    analysis = '''\
The AI-suggested code uses Python’s built-in sorted() function with a lambda expression, resulting in a time complexity of O(n log n). It is concise, readable, and leverages optimized internal algorithms. The manual implementation uses nested loops, leading to O(n²) complexity, which is less efficient for large datasets. The AI-generated version is preferable for its performance, maintainability, and clarity. Manual approaches are more error-prone and harder to maintain, especially as data size grows. In practice, using language features and libraries, as suggested by AI tools, leads to better code quality and developer productivity.
'''
    print(analysis)
