import matplotlib.pyplot as plt
import numpy as np

def calculate_child_growth(start_height, start_weight, start_age_years, target_age=12):
    """
    專門模擬 0-12 歲的生長數據
    """
    ages = []
    heights = []
    weights = []
    
    current_h = start_height
    current_w = start_weight
    
    # 模擬從當前年齡到 12 歲，以「月」為單位
    start_month = int(start_age_years * 12)
    end_month = int(target_age * 12)
    
    for month in range(start_month, end_month + 1):
        age_y = month / 12
        ages.append(age_y)
        heights.append(current_h)
        weights.append(current_w)
        
        # --- 0-12 歲細分生長速率 (公分/月, 公斤/月) ---
        if age_y < 1:
            hr, wr = 2.0, 0.5    # 0-1歲：極速成長期 (一年約長24cm)
        elif age_y < 2:
            hr, wr = 1.0, 0.25   # 1-2歲：快速成長期
        elif age_y < 4:
            hr, wr = 0.6, 0.14    # 2-4歲：穩定期
        elif age_y < 6:
            hr, wr = 0.45, 0.14  # 4-6歲：平穩期
        elif age_y < 9:
            hr, wr = 0.45, 0.2  # 6-9歲：衝刺前期
        else:
            hr, wr = 0.55, 0.35  # 9-12歲：青春期前期 (準備衝刺)
            
        current_h += hr
        current_w += wr

    return ages, heights, weights

# 設定初始參數 (假設從出生開始：50cm, 3.3kg)
age_axis, height_axis, weight_axis = calculate_child_growth(50, 3.3, 0)

# --- 圖表美化設定 ---
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

fig, ax1 = plt.subplots(figsize=(10, 6))

# 繪製身高 (左軸)
ax1.set_xlabel('年齡 (歲)', fontsize=12)
ax1.set_ylabel('身高 (cm)', color='royalblue', fontsize=12)
ax1.plot(age_axis, height_axis, color='royalblue', linewidth=2.5, label='身高 (cm)')
ax1.tick_params(axis='y', labelcolor='royalblue')
ax1.set_xticks(np.arange(0, 13, 1)) # 設定 0-12 歲刻度
ax1.grid(True, which='both', linestyle='--', alpha=0.5)

# 繪製體重 (右軸)
ax2 = ax1.twinx()
ax2.set_ylabel('體重 (kg)', color='crimson', fontsize=12)
ax2.plot(age_axis, weight_axis, color='crimson', linewidth=2.5, linestyle='-.', label='體重 (kg)')
ax2.tick_params(axis='y', labelcolor='crimson')

# 加入標註
plt.title('0-12 歲兒童生長模擬曲線圖', fontsize=16, pad=20)
fig.tight_layout()

# 顯示數值參考 (顯示 12 歲預期值)
final_h = height_axis[-1]
final_w = weight_axis[-1]
plt.annotate(f'12歲預期: {final_h:.1f}cm\n{final_w:.1f}kg', 
             xy=(12, final_h), xycoords='data',
             xytext=(-100, -40), textcoords='offset points',
             arrowprops=dict(arrowstyle="->", color='black'))

plt.show()