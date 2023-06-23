

"""
Example 8.13 (modified): medical treatment probability of success
=================================================================

"""

import sys
import math
import numpy as np
import plotly.graph_objects as go

#%%
# prior function
def prior(success_rate):
    return 1.0 / 101


#%%
# likelihood function
def likelihood(num_successes, success_rate, num_tests=10):
    answer = (math.comb(num_tests, num_successes) * success_rate**num_successes *
              (1 - success_rate)**(num_tests-num_successes))
    return answer


#%%
# define variables
num_tests = 10
true_success_rate = 0.7
num_observations = 30
num_bins_succeses = 101

#%%
# computer prior
success_rates = [float(i)/num_bins_succeses
                 for i in range(num_bins_succeses)]
obs_num_successes = np.random.binomial(n=num_tests, p=true_success_rate,
                                       size=num_observations)
current_prior = np.array([prior(success_rate=success_rate)
                          for success_rate in success_rates])
#%%
# plot prior
i = -1
fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_prior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 1 observation
i = 1
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 2 observations
i = 2
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 3 observations
i = 3
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 4 observations
i = 4
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 5 observations
i = 5
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 6 observations
i = 6
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 7 observations
i = 7
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 8 observations
i = 8
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 9 observations
i = 9
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 10 observations
i = 10
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 11 observations
i = 11
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 12 observations
i = 12
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 13 observations
i = 13
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 14 observations
i = 14
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 15 observations
i = 15
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 16 observations
i = 16
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 17 observations
i = 17
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 18 observations
i = 18
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 19 observations
i = 19
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 20 observations
i = 20
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 21 observations
i = 21
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 22 observations
i = 22
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 23 observations
i = 23
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 24 observations
i = 24
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 25 observations
i = 25
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 26 observations
i = 26
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 27 observations
i = 27
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 28 observations
i = 28
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig

#%%
# computer and plot posteriors for 29 observations
i = 29
an_obs_num_successes = obs_num_successes[i]
current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                          success_rate=success_rate)
                               for success_rate in success_rates])
current_posterior = current_prior * current_likelihood
current_posterior /= np.sum(current_posterior)
current_prior = current_posterior

fig = go.Figure()
trace = go.Bar(x=success_rates, y=current_posterior)
fig.add_trace(trace)
fig.add_vline(x=true_success_rate, line_color="red")
fig.update_layout(xaxis_title="Success Rate",
                  yaxis_title="Probability",
                  title=(f"Number Observations {i+1}, "
                         f"True Prob. Success {true_success_rate}"))
fig
