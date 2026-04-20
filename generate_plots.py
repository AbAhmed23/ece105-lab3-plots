import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    rng = np.random.default_rng(seed)
    sensor_a = rng.normal(25, 3, 200)
    sensor_b = rng.normal(27, 4.5, 200)
    timestamps = rng.uniform(0, 10, 200)
    return sensor_a, sensor_b, timestamps


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    ax.scatter(timestamps, sensor_a, label="Sensor A")
    ax.scatter(timestamps, sensor_b, label="Sensor B")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Scatter Plot")
    ax.legend()


def plot_histogram(sensor_a, sensor_b, ax):
    ax.hist(sensor_a, bins=30, alpha=0.5, label="Sensor A")
    ax.hist(sensor_b, bins=30, alpha=0.5, label="Sensor B")
    ax.axvline(sensor_a.mean(), linestyle="dashed")
    ax.axvline(sensor_b.mean(), linestyle="dashed")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram")
    ax.legend()


def plot_boxplot(sensor_a, sensor_b, ax):
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.boxplot([sensor_a, sensor_b], tick_labels=["Sensor A", "Sensor B"])
    ax.axhline(overall_mean, linestyle="dashed")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Box Plot")


def main():
    sensor_a, sensor_b, timestamps = generate_data(1234)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])
    plot_boxplot(sensor_a, sensor_b, axes[2])

    plt.tight_layout()
    plt.savefig("sensor_analysis.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()