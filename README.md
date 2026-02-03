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


# legged_control : 다족 보행 로봇 NMPC
  - https://github.com/qiayuanl/legged_control

# quadruped_nmpc_dcbf_duality : 다족 보행 로봇의 좁은 환경에서의 이중성 기반 최적화
  - https://github.com/HybridRobotics/quadruped_nmpc_dcbf_duality
  - 이중성 기반 최적화 : 원 문제(primal) + 이중 문제(dual)의 이중성을 이용하는 최적화
        - 보통 원 문제는 직접 비용함수를 최소로 하는 제어 입력을 구하는 것이고, 이중 문제는 라그랑주 승수를 이용하여 직접적으로 제어입력을 알아내는 것이 아닌, 벌칙(penalty)를 계산하여 이를 최대로 하는 지점을 구하는 것.
    
  - 라그랑주 이중성(Lagrangian Duality) : 원문제는 제약을 무조건 지키면서 최소화해야하는 반면, 이중 문제의 경우 u에 대해 최소화한 함수를 만들고 벌금 계수 람다를 조절하며 최대화할 수 있다.

  - https://arxiv.org/pdf/2212.14199

  - 
