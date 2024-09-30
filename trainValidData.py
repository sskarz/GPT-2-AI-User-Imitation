import random

# Set random seed for reproducibility
random.seed(42)

# Load data
with open("tokenized_sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Shuffle data
random.shuffle(lines)

# Split data: 80% for training and 20% for validation
train_size = int(0.8 * len(lines))
train_data = lines[:train_size]
valid_data = lines[train_size:]

# Save training data
with open("train_data.txt", "w", encoding="utf-8") as f:
    f.writelines(train_data)

# Save validation data
with open("valid_data.txt", "w", encoding="utf-8") as f:
    f.writelines(valid_data)

print(f"Saved {len(train_data)} lines of training data to 'train_data.txt'")
print(f"Saved {len(valid_data)} lines of validation data to 'valid_data.txt'")
