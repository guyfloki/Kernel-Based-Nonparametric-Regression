
import matplotlib.pyplot as plt

def plot_estimations(true_x, true_y, sample_x, sample_y, estimations, labels, title="Estimation Comparison"):
    fig, axs = plt.subplots(1, 3, figsize=(24, 6))
    linestyles = ['dashed', 'dotted', 'dashdot']
    
    # Plotting the true function and sample data on all subplots
    for ax in axs:
        ax.plot(true_x, true_y, label="True Function", color="blue")
        ax.scatter(sample_x, sample_y, color='red', s=15, label="Sample Data")
        ax.legend()
        ax.grid(True)
    
    # Plotting each estimator on a separate subplot
    for est, label, ls, ax in zip(estimations, labels, linestyles, axs):
        ax.plot(true_x, est, label=label, linestyle=ls)
        ax.set_title(label)
        ax.set_xlabel("x")
    
    axs[0].set_ylabel("y")
    plt.suptitle(title)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    plt.savefig("kernels.png")
    plt.show()

