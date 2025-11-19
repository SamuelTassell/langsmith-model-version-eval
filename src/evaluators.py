"""Custom evaluators for model comparison."""
from typing import Dict, Any, Callable


def correctness_evaluator(
    output: str,
    expected: str,
    comparison_fn: Callable[[str, str], bool] = None
) -> Dict[str, Any]:
    """
    Evaluate the correctness of a model output.
    
    Args:
        output: The actual output from the model
        expected: The expected output
        comparison_fn: Optional custom comparison function
    
    Returns:
        dict: Evaluation result with 'correct' boolean and 'details'
    """
    if comparison_fn:
        correct = comparison_fn(output, expected)
    else:
        # Simple exact match by default
        correct = output.strip().lower() == expected.strip().lower()
    
    return {
        "correct": correct,
        "output": output,
        "expected": expected,
        "details": "Match" if correct else "Mismatch"
    }


def latency_evaluator(latency: float, threshold: float = 5.0) -> Dict[str, Any]:
    """
    Evaluate the latency of a model response.
    
    Args:
        latency: Response latency in seconds
        threshold: Maximum acceptable latency in seconds
    
    Returns:
        dict: Evaluation result with performance assessment
    """
    within_threshold = latency <= threshold
    
    performance = "excellent" if latency < threshold * 0.5 else \
                 "good" if latency < threshold * 0.75 else \
                 "acceptable" if within_threshold else "poor"
    
    return {
        "latency": latency,
        "threshold": threshold,
        "within_threshold": within_threshold,
        "performance": performance
    }


def combined_evaluator(
    output: str,
    expected: str,
    latency: float,
    latency_threshold: float = 5.0
) -> Dict[str, Any]:
    """
    Combined evaluation of correctness and latency.
    
    Args:
        output: The actual output from the model
        expected: The expected output
        latency: Response latency in seconds
        latency_threshold: Maximum acceptable latency
    
    Returns:
        dict: Combined evaluation results
    """
    correctness = correctness_evaluator(output, expected)
    latency_eval = latency_evaluator(latency, latency_threshold)
    
    return {
        **correctness,
        **latency_eval,
        "overall_pass": correctness["correct"] and latency_eval["within_threshold"]
    }
