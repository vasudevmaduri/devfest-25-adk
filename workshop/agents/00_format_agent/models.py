from pydantic import BaseModel, Field
from typing import List, Optional

class FeatureComparison(BaseModel):
    feature_name: str = Field(..., description="The name of the feature being compared (e.g., 'Camera', 'Battery').")
    product_a_value: str = Field(..., description="The value/spec for the first product.")
    product_b_value: str = Field(..., description="The value/spec for the second product.")
    winner: str = Field(..., description="Which product wins this category, or 'Tie'.")

class Product(BaseModel):
    name: str = Field(..., description="Name of the product.")
    price: str = Field(..., description="Approximate price.")
    pros: List[str] = Field(..., description="List of key advantages.")
    cons: List[str] = Field(..., description="List of key disadvantages.")

class ComparisonReport(BaseModel):
    """A structured report comparing two products."""
    product_a: Product
    product_b: Product
    feature_comparisons: List[FeatureComparison]
    final_verdict: str = Field(..., description="A summary conclusion on which product is better for whom.")
