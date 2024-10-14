from PIL import Image

def merge_images(image_path1, image_path2, output_path):
    # 打開兩張圖片
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)

    # 獲取兩張圖片的尺寸
    img1_width, img1_height = img1.size
    img2_width, img2_height = img2.size

    # 計算合併後的寬度和高度 (取最高的圖片高度)
    total_width = img1_width + img2_width
    max_height = max(img1_height, img2_height)

    # 建立一個新的空白圖片，尺寸為合併後的總寬度和最大高度
    merged_image = Image.new('RGB', (total_width, max_height))

    # 將兩張圖片貼到新建的圖片上
    merged_image.paste(img1, (0, 0))  # 左邊放第一張圖片
    merged_image.paste(img2, (img1_width, 0))  # 右邊放第二張圖片

    # 儲存合併後的圖片
    merged_image.save(output_path)
    print(f"圖片已成功合併並儲存至 {output_path}")

# 使用範例
image1 = 'TF/week6/hw1.png'
image2 = 'TF/week6/hw2.png'
output_image = 'merged_image.jpg'
merge_images(image1, image2, output_image)
