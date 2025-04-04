# coding:UTF-8

from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, pair

def setup(group):
    """
    系统初始化，生成系统参数
    """
    P = group.random(G1)  # G1 生成元
    s = group.random(ZR)  # 系统主密钥
    pk_sys = s * P  # 系统公钥
    return P, s, pk_sys

def keygen(group, s, ID):
    """
    用户密钥生成
    """
    Q_ID = group.hash(ID, G1)  # 公钥 Q_ID = H1(ID)
    d_ID = s * Q_ID  # 私钥 d_ID = s * Q_ID
    return Q_ID, d_ID

def sign(group, P, d_ID, message):
    """
    签名生成
    """
    k = group.random(ZR)  # 随机数 k
    R = k * P  # 计算 R = kP
    H_m = group.hash(message, G1)  # 哈希消息到 G1
    S = k * H_m + d_ID  # 计算 S = kH2(m) + d_ID
    return R, S

def verify(group, P, pk_sys, Q_ID, message, signature):
    """
    签名验证
    """
    R, S = signature
    H_m = group.hash(message, G1)  # 哈希消息到 G1
    # 验证公式：e(S, P) == e(H2(m), R) * e(Q_ID, P_sys)
    left = pair(S, P)
    right = pair(H_m, R) * pair(Q_ID, pk_sys)
    return left == right

if __name__ == "__main__":
    # 初始化配对群
    group = PairingGroup('SS512')

    # 系统初始化
    P, s, pk_sys = setup(group)
    print("生成元 P:", P)
    print("系统主密钥 s:", s)
    print("系统公钥 pk_sys:", pk_sys)

    # 用户密钥生成
    ID = "user@example.com"
    Q_ID, d_ID = keygen(group, s, ID)
    print("用户公钥 Q_ID:", Q_ID)
    print("用户私钥 d_ID:", d_ID)

    # 消息签名
    message = "Hello, World!"
    signature = sign(group, P, d_ID, message)
    print("签名 (R, S):", signature)

    # 签名验证
    is_valid = verify(group, P, pk_sys, Q_ID, message, signature)
    print("签名验证结果:", is_valid)





