"""Utility functions for model evaluation."""
from typing import Dict, Any, List
import time


def measure_latency(func, *args, **kwargs) -> tuple[Any, float]:
    """
    Measure the latency of a function call.
    
    Args:
        func: The function to measure
        *args: Positional arguments for the function
        **kwargs: Keyword arguments for the function
    
    Returns:
        tuple: (result, latency_in_seconds)
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    latency = end_time - start_time
    
    return result, latency


def format_evaluation_results(results: List[Dict[str, Any]]) -> str:
    """
    Format evaluation results for display.
    
    Args:
        results: List of evaluation result dictionaries
    
    Returns:
        str: Formatted results string
    """
    if not results:
        return "No results to display"
    
    output = []
    output.append(f"Total evaluations: {len(results)}")
    output.append("-" * 50)
    
    for i, result in enumerate(results, 1):
        output.append(f"\nEvaluation {i}:")
        for key, value in result.items():
            output.append(f"  {key}: {value}")
    
    return "\n".join(output)


def calculate_metrics(results: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calculate aggregate metrics from evaluation results.
    
    Args:
        results: List of evaluation result dictionaries
    
    Returns:
        dict: Aggregate metrics
    """
    if not results:
        return {}
    
    metrics = {
        "total_count": len(results),
        "avg_latency": sum(r.get("latency", 0) for r in results) / len(results),
    }
    
    # Calculate correctness if available
    if any("correct" in r for r in results):
        correct_count = sum(1 for r in results if r.get("correct", False))
        metrics["correctness_rate"] = correct_count / len(results)
    
    return metrics
