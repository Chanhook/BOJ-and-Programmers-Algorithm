n, m, k = map(int, input().split())

for m_need in range(1, m + 1):
    m_left, w_left, w_need = m - m_need, n - 2 * m_need, 2 * m_need
    if m_left < 0 or w_left < 0 or m_left + w_left - k < 0:
        print(m_need - 1)
        break
    if m_need == m:
        print(m_need)
