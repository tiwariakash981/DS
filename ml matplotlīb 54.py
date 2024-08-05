import matplotlib.pyplot as plt
import matplotlib.image as img

img1 = img.imread(r'C:\AKASH\PIE.png')
print(img1)

print(img1.shape)
print(img1.ndim)
print(type(img1))

##plt.figure(figsize=(16,9))
single_channel=img1[:,:,1]
plt.imshow(single_channel,cmap='hot')
plt.axis('off')
plt.colorbar()##side me jo bar aa rha hai vo
plt.show()

single_channel2=img1[:,:,0]
plt.imshow(single_channel2,cmap='nipy_spectral')
plt.axis('off')
plt.colorbar()##side me jo bar aa rha hai vo
plt.show()

























 










