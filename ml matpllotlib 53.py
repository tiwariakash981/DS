import matplotlib.pyplot as plt
import matplotlib.image as img

img1 = img.imread(r'C:\AKASH\PIE.png')
print(img1)

print(img1.shape)
print(img1.ndim)
print(type(img1))

##plt.figure(figsize=(16,9))
plt.imshow(img1,cmap='hot')
plt.axis('off')
plt.colorbar()##side me jo bar aa rha hai vo
plt.show()



























 










