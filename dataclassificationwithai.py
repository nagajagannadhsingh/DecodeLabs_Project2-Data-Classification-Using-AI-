import numpy as np
import matplotlib.pyplot as plt
# ==========================================================
# 1. CREATE SMALL DATASET
# ==========================================================
# Features:
# [sepal length, sepal width, petal length, petal width]
X = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [4.7, 3.2, 1.3, 0.2],
    [4.6, 3.1, 1.5, 0.2],
    [5.0, 3.6, 1.4, 0.2],

    [5.4, 3.9, 1.7, 0.4],
    [4.6, 3.4, 1.4, 0.3],
    [5.0, 3.4, 1.5, 0.2],
    [4.4, 2.9, 1.4, 0.2],
    [4.9, 3.1, 1.5, 0.1],

    [6.0, 2.9, 4.5, 1.5],
    [5.7, 2.8, 4.5, 1.3],
    [6.3, 3.3, 4.7, 1.6],
    [5.6, 2.9, 3.6, 1.3],
    [5.5, 2.6, 4.4, 1.2],

    [6.7, 3.0, 5.2, 2.3],
    [6.3, 2.9, 5.6, 1.8],
    [6.5, 3.0, 5.8, 2.2],
    [7.1, 3.0, 5.9, 2.1],
    [6.3, 2.5, 5.0, 1.9]
])
# Class labels
# 0 = Setosa
# 1 = Versicolor
# 2 = Virginica
y = np.array([
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1,
    2, 2, 2, 2, 2
])
class_names = [
    "Setosa",
    "Versicolor",
    "Virginica"
]
print("=" * 60)
print("DECODELABS PROJECT 2")
print("DATA CLASSIFICATION USING AI")
print("=" * 60)
# ==========================================================
# 2. UNDERSTAND DATASET
# =========================================================
print("\nDataset shape:")
print(X.shape)
print("\nNumber of samples:", len(X))
print("\nNumber of features:", X.shape[1])
print("\nFirst 5 records:")
print(X[:5])
print("\nClass names:")
print(class_names)
# ==========================================================
# 3. SPLIT DATA INTO TRAINING AND TESTING
# =========================================================
np.random.seed(42)
indices = np.random.permutation(len(X))
train_size = int(0.8 * len(X))
train_indices = indices[:train_size]
test_indices = indices[train_size:]
X_train = X[train_indices]
X_test = X[test_indices]
y_train = y[train_indices]
y_test = y[test_indices]
print("\nTraining samples:", len(X_train))
print("Testing samples :", len(X_test))
# ==========================================================
# 4. FEATURE SCALING
# ==========================================================
mean = np.mean(X_train, axis=0)
std = np.std(X_train, axis=0)
X_train_scaled = (
    X_train - mean
) / std
X_test_scaled = (
    X_test - mean
) / std
print("\nFeature scaling completed.")
# ==========================================================
# 5. KNN FUNCTION
# ==========================================================
def knn_predict(
    X_train,
    y_train,
    X_test,
    k
):
    predictions = []
    for test_point in X_test:
        # Calculate Euclidean distance
        distances = np.sqrt(
            np.sum(
                (X_train - test_point) ** 2,
                axis=1
            )
        )
        # Find nearest points
        nearest_indices = np.argsort(
            distances
        )[:k]
        nearest_labels = y_train[
            nearest_indices
        ]
        # Find most common class
        values, counts = np.unique(
            nearest_labels,
            return_counts=True
        )
        prediction = values[
            np.argmax(counts)
        ]
        predictions.append(
            prediction
        )
    return np.array(predictions)
# ==========================================================
# 6. TEST DIFFERENT VALUES OF K
# ==========================================================
k_values = [1, 3, 5, 7]
accuracies = []
print("\nK Selection")
print("-" * 40)
for k in k_values:
    predictions = knn_predict(
        X_train_scaled,
        y_train,
        X_test_scaled,
        k
    )
    accuracy = np.mean(
        predictions == y_test
    )
    accuracies.append(
        accuracy
    )
    print(
        "K =", k,
        "Accuracy =",
        round(accuracy, 4)
    )
# Select best K
best_index = np.argmax(
    accuracies
)
best_k = k_values[
    best_index
]
best_accuracy = accuracies[
    best_index
]
print("\nBest K:", best_k)
print(
    "Best Accuracy:",
    round(best_accuracy, 4)
)
# ==========================================================
# 7. FINAL PREDICTION
# ==========================================================
final_predictions = knn_predict(
    X_train_scaled,
    y_train,
    X_test_scaled,
    best_k
)
# ==========================================================
# 8. ACCURACY
# ==========================================================
accuracy = np.mean(
    final_predictions == y_test
)
print("\n")
print("=" * 60)
print("MODEL EVALUATION")
print("=" * 60)
print(
    "\nAccuracy:",
    round(accuracy * 100, 2),
    "%"
)
# ==========================================================
# 9. CONFUSION MATRIX
# ==========================================================
confusion = np.zeros(
    (3, 3),
    dtype=int
)
for actual, predicted in zip(
    y_test,
    final_predictions
):
    confusion[
        actual,
        predicted
    ] += 1
print("\nConfusion Matrix:")
print(confusion)
# ==========================================================
# 10. PRECISION, RECALL AND F1 SCORE
# ==========================================================
precision_values = []
recall_values = []
f1_values = []
for class_id in range(3):
    true_positive = confusion[
        class_id,
        class_id
    ]
    false_positive = (
        np.sum(confusion[:, class_id])
        - true_positive
    )
    false_negative = (
        np.sum(confusion[class_id, :])
        - true_positive
    )
    if (
        true_positive +
        false_positive
    ) > 0:
        precision = (
            true_positive /
            (
                true_positive +
                false_positive
            )
        )
    else:
        precision = 0
    if (
        true_positive +
        false_negative
    ) > 0:
        recall = (
            true_positive /
            (
                true_positive +
                false_negative
            )
        )
    else:
        recall = 0
    if precision + recall > 0:
        f1 = (
            2 *
            precision *
            recall /
            (precision + recall)
        )
    else:
        f1 = 0
    precision_values.append(
        precision
    )
    recall_values.append(
        recall
    )
    f1_values.append(
        f1
    )
precision = np.mean(
    precision_values
)
recall = np.mean(
    recall_values
)
f1 = np.mean(
    f1_values
)
print(
    "Precision:",
    round(precision, 4)
)
print(
    "Recall   :",
    round(recall, 4)
)
print(
    "F1 Score :",
    round(f1, 4)
)
# ==========================================================
# 11. PREDICT NEW DATA
# ==========================================================
new_data = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [6.0, 2.9, 4.5, 1.5],
    [6.7, 3.0, 5.2, 2.3]
])
new_data_scaled = (
    new_data - mean
) / std
new_predictions = knn_predict(
    X_train_scaled,
    y_train,
    new_data_scaled,
    best_k
)
print("\n")
print("=" * 60)
print("NEW DATA PREDICTIONS")
print("=" * 60)
for sample, prediction in zip(
    new_data,
    new_predictions
):
    print(
        sample,
        "->",
        class_names[prediction]
    )
# ==========================================================
# 12. CONFUSION MATRIX VISUALIZATION
# ==========================================================
plt.figure(figsize=(7, 5))
plt.imshow(confusion)
plt.title(
    "Confusion Matrix - KNN"
)
plt.xlabel(
    "Predicted Class"
)
plt.ylabel(
    "Actual Class"
)
plt.xticks(
    [0, 1, 2],
    class_names
)
plt.yticks(
    [0, 1, 2],
    class_names
)
for i in range(3):
    for j in range(3):
        plt.text(
            j,
            i,
            confusion[i][j],
            ha="center",
            va="center"
        )
plt.colorbar()
plt.tight_layout()
plt.show()
print("\nProject completed successfully!")