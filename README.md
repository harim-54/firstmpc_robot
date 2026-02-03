# firstmpc_robot
My first mpc control for robot competition.


# MPPI control(26.02.03)

MPC control 
Receding Horizon Control : 후퇴 예측 제어

1. Practical NMPC suboptimality estimates along trajectories
  일반적으로 계산적으로 다루기 어려운 무한 예측 최적 제어 문제의 해를 유한 예측 최적 제어 문제의 시퀀스로 근사화하는 방식.
  다음 결과 제어 시퀀스의 첫 번째 요소가 각 시간 단계에서 구현되어 폐루프 정적 상태 피드백을 생성.

  무한 시간 범위 문제의 근사화는 자연스럽게 결과적인 MPC 피드백의 쵲거성 부족 문제에 대한 질문으로 이어짐.
  
    주요 과제는 : 무한 시간 범위 비용 함수에 대한 MPC 피드백의 최적성 부족 정도, 안정성을 추정해야함.

  임의의 거리 공간에서 이산 시간 비선형 시스템을 다루고, 종단 비용이나 종단 제약 조건이 없는 유한 시간 범위 최적 제어 문제를 사용.
  폐루프 궤적을 따라 온라인으로 최적성 부족 정도를 추정하는 기법 

  - 시간 범위 축소 접근법 (receding horizon approach) : 무한 시간 범위 최적 제어 문제는 필연적으로 HJB equation을 풀어야하기 때문에 무한 시간 범위의 최적 제어 문제를 유한 시간 범위 최적 제어 문제들의 연속으로 대체하는 과정이 필요함.

  - https://www.sciencedirect.com/science/article/pii/S0167691108001795

