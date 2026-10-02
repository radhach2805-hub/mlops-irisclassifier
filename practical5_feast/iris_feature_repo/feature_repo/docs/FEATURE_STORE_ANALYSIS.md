# Feature Store Analysis

## Benefits Observed

### 1. Elimination of Training-Serving Skew

The same iris engineered features are used for both online and offline retrieval.

This means the feature definitions are not separately implemented for training and serving.

### 2. Feature Reusability

The registered features can be reused by another model or ML task without implementing the feature calculations again.

### 3. Centralized Governance

The file features.py acts as a central definition for the features.

This provides a single source of truth for the consuming models.