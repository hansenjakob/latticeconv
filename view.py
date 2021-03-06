import numpy as np
import torch
from matplotlib import pyplot as plt

lattice_train_accuracy = torch.load('./lattice_train_accuracy_t15.pt')
lattice_test_accuracy = torch.load('./lattice_test_accuracy_t15.pt')
lattice_train_loss = torch.load('./lattice_train_loss_t15.pt')
conv_train_accuracy = torch.load('./conv_train_accuracy_t15.pt')
conv_test_accuracy = torch.load('./conv_test_accuracy_t15.pt')
conv_train_loss = torch.load('./conv_train_loss_t15.pt')

# fc_train_accuracy = torch.load('./fc_train_accuracy.pt')
# fc_test_accuracy = torch.load('./fc_test_accuracy.pt')
#hybrid_train_accuracy = torch.load('./hybrid_train_accuracy_t20.pt')
#hybrid_test_accuracy = torch.load('./hybrid_test_accuracy_t20.pt')
#hybrid_train_loss = torch.load('./hybrid_train_loss_t20.pt')

#n = len(conv_train_accuracy)
n = len(lattice_train_accuracy)

plt.figure(1)
plt.errorbar(1+np.arange(n),lattice_train_accuracy.mean(axis=1),lattice_train_accuracy.std(axis=1), label='Lattice-based CNN')
#plt.errorbar(1+np.arange(n),conv_train_accuracy.mean(axis=1), conv_train_accuracy.std(axis=1),label='Classical CNN', alpha=0.5)
#plt.errorbar(1+np.arange(n),fc_train_accuracy.mean(axis=1), fc_train_accuracy.std(axis=1),label='fc', alpha=0.5)
#plt.errorbar(1+np.arange(n),hybrid_train_accuracy.mean(axis=1), hybrid_train_accuracy.std(axis=1),label='Hybrid CNN', alpha=0.5)

plt.legend()
plt.title('Training accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.ylim((0, 1))
plt.xlim((0, n+1))
plt.savefig('./plots/train/'+name)
plt.show()


plt.figure(2)
plt.errorbar(1+np.arange(n), lattice_test_accuracy.mean(axis=1), lattice_test_accuracy.std(axis=1), label='Lattice-based CNN')
#plt.errorbar(1+np.arange(n), conv_test_accuracy.mean(axis=1), conv_test_accuracy.std(axis=1), label='Classical CNN', alpha=0.5)
#plt.errorbar(1+np.arange(n),fc_test_accuracy.mean(axis=1), fc_test_accuracy.std(axis=1),label='fc', alpha=0.5)
#plt.errorbar(1+np.arange(n),hybrid_test_accuracy.mean(axis=1), hybrid_test_accuracy.std(axis=1),label='Hybrid CNN', alpha=0.5)

plt.legend()
plt.title('Testing accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.ylim((0, 1))
plt.xlim((0, n+1))
plt.savefig('./plots/test/'+name)
plt.show()

#plt.figure(3)
#for i in range(10):
#    plt.plot(1+np.arange(n), lattice_train_loss[:,i])
#plt.show()
plt.figure(3)
plt.errorbar(1+np.arange(n), lattice_train_loss.mean(axis=1), lattice_train_loss.std(axis=1), label='Lattice-based CNN')
plt.errorbar(1+np.arange(n), conv_train_loss.mean(axis=1), conv_train_loss.std(axis=1), label='Classical CNN', alpha=0.5)
#plt.errorbar(1+np.arange(n),fc_test_accuracy.mean(axis=1), fc_test_accuracy.std(axis=1),label='fc', alpha=0.5)
#plt.errorbar(1+np.arange(n),hybrid_train_loss.mean(axis=1), hybrid_train_loss.std(axis=1),label='Hybrid CNN', alpha=0.5)
plt.yscale("log")
plt.legend()
plt.title('Training loss')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.ylim((0, 1))
plt.xlim((0, n+1))
plt.show()