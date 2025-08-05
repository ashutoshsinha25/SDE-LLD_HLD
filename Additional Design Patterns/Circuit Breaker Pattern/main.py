# Circuit Breaker Pattern Example 

import os 
import time 
import random 
from typing import Callable, Any 

class CircuitBreaker:
    def __init__(self, failure_threshold: int, recovery_timeout: int):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = 'CLOSED'  # Possible states: CLOSED, OPEN, HALF_OPEN

    def call(self, func: Callable[[], Any]) -> Any:
        if self.state == 'OPEN':
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = 'HALF_OPEN'
            else:
                raise Exception("Circuit is open. Cannot execute function.")

        try:
            result = func()
            self.reset()
            return result
        except Exception as e:
            self.record_failure()
            raise e

    def record_failure(self):
        self.failure_count += 1
        if self.failure_count >= self.failure_threshold:
            self.state = 'OPEN'
            self.last_failure_time = time.time()

    def reset(self):
        self.failure_count = 0
        if self.state == 'HALF_OPEN':
            self.state = 'CLOSED'
    def __str__(self):
        return f"CircuitBreaker(state={self.state}, failure_count={self.failure_count})"
    
def unreliable_function():
    if random.random() < 0.7:  # 70% chance of failure
        raise Exception("Function failed!")
    return "Function succeeded!"

if __name__ == "__main__":
    breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=5)

    for i in range(10):
        try:
            result = breaker.call(unreliable_function)
            print(f"Attempt {i + 1}: {result}")
        except Exception as e:
            print(f"Attempt {i + 1}: {e}")
        
        time.sleep(1)  # Simulate time between attempts
        print(breaker)  # Print the state of the circuit breaker

# usecase:
# This code demonstrates a simple Circuit Breaker pattern implementation.
# It simulates a function that fails 70% of the time and uses the Circuit Breaker to manage failures.
# The Circuit Breaker transitions between CLOSED, OPEN, and HALF_OPEN states based on the number of failures and recovery timeout.

# code run:
# Attempt 1: Function succeeded!
# CircuitBreaker(state=CLOSED, failure_count=0)
# Attempt 2: Function succeeded!
# CircuitBreaker(state=CLOSED, failure_count=0)
# Attempt 3: Function succeeded!
# CircuitBreaker(state=CLOSED, failure_count=0)
# Attempt 4: Function failed!
# CircuitBreaker(state=CLOSED, failure_count=1)
# Attempt 5: Function failed!
# CircuitBreaker(state=CLOSED, failure_count=2)
# Attempt 6: Function failed!
# CircuitBreaker(state=OPEN, failure_count=3)
# Attempt 7: Circuit is open. Cannot execute function.
# CircuitBreaker(state=OPEN, failure_count=3)
# Attempt 8: Circuit is open. Cannot execute function.
# CircuitBreaker(state=OPEN, failure_count=3)
# Attempt 9: Circuit is open. Cannot execute function.
# CircuitBreaker(state=OPEN, failure_count=3)
# Attempt 10: Circuit is open. Cannot execute function.
# CircuitBreaker(state=OPEN, failure_count=3)

