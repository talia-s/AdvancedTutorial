# Training and Evaluating the Baseline Model

Now that your data is prepared, let's train a model that predicts the vertex
position from detector hits.

We've provided a 
[pre-built model](https://github.com/TRISEP-2025-ML-tutorials/AdvancedTutorial/blob/main/code/model/regressor.py)
and a
[training script](https://github.com/TRISEP-2025-ML-tutorials/AdvancedTutorial/blob/main/code/train.py),
which you can run like:

```bash
python train.py /path/to/train.parquet /path/to/validate.parquet --output-dir /path/to/output
```

This will run a full training loop and create the following files in the
`/path/to/output` directory:
- `config.toml`: the hyperparameters used during training.
- `training_log.csv`: a CSV file with the training and validation loss at each
  epoch.
- `model.pt`: the trained model.

Training the model can take a while depending on the size of your dataset, the
number of epochs, and the hardware you are using. By default, the training
script will run for 50 epochs. You can inspect the `training_log.csv` file to
monitor training progress.

> **Activity:**  
> Write a script to plot the training and validation loss as a function of
> epoch.  
> What do you observe?

Once the model is trained, you can evaluate how well it performs on the
validation set using the provided
[test script](https://github.com/TRISEP-2025-ML-tutorials/AdvancedTutorial/blob/main/code/test.py):

```bash
python test.py /path/to/model.pt /path/to/validate.parquet --output /path/to/output.csv
```

This will create a CSV file with both the true and predicted vertex positions
for each event.

> **Activity:**  
> - Write a script to plot predicted vertex position vs. true vertex position.
> - Create a histogram of the residuals (predicted - true).
> - Plot the residuals as a function of true z-position. Is there any pattern?

If you finish early or are curious to experiment, try following the **bonus
activity** to see how a small change can impact model performance. Otherwise,
feel free to jump ahead to **Session 2**, where we'll explore the model in more
depth.

## Bonus Activity (Optional)

You've now trained and evaluated a baseline model. Let's tweak one component to
see what happens!

Try changing the loss function
[here](https://github.com/TRISEP-2025-ML-tutorials/AdvancedTutorial/blob/main/code/training/loss.py#L25)
from **Mean Squared Error** to
[**Mean Absolute Error**](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.l1_loss.html).

Then retrain the model and evaluate it again.
