def value_iteration():
  prod_actions = {'coding': ["productive", 0.2, 30, "exhausted", 0.8, 40], 'exercise': ["fit", 1, -10], 'rest': ["productive", 1, 0]}
  exh_actions = {'coding': ["exhausted", 1, 20], 'exercise': ["productive", 0.5, -10, "exhausted", 0.5, -10], 'rest': ["productive", 0.8, 0, "exhausted", 0.2, 0]}
  fit_actions = {'coding':["exhausted", 1, 100], 'exercise': ["fit", 1, 0], 'rest': ["fit", 1, 0]}
  discount = 0.86

  prod_opt_prev = 0
  prod_opt_curr = 0

  exh_opt_prev = 0
  exh_opt_curr = 0

  fit_opt_prev = 0
  fit_opt_curr = 0

  opt_value_prev = 0
  opt_value_curr = 0

  stable_prod_value = 0
  stable_exh_value = 0
  stable_fit_value = 0

  prod_opt_policy = ""
  exh_opt_policy = ""
  fit_opt_policy = ""

  iterations = 1

  while True:
    prod_opt_curr, prod_opt_policy = state_opt_curr(prod_actions, iterations, discount, prod_opt_prev, exh_opt_prev, fit_opt_prev)
    exh_opt_curr, exh_opt_policy = state_opt_curr(exh_actions, iterations, discount, prod_opt_prev, exh_opt_prev, fit_opt_prev)
    fit_opt_curr, fit_opt_policy = state_opt_curr(fit_actions, iterations, discount, prod_opt_prev, exh_opt_prev, fit_opt_prev)

    if abs(prod_opt_prev - prod_opt_curr) <= 0.01:
      stable_prod_value = prod_opt_curr
      if abs(exh_opt_prev - exh_opt_curr) <= 0.01:
        stable_exh_value = exh_opt_curr
        if abs(fit_opt_prev - fit_opt_curr) <= 0.01:
          stable_fit_value = fit_opt_curr
          break
    else:
      prod_opt_prev = prod_opt_curr
      exh_opt_prev = exh_opt_curr
      fit_opt_prev = fit_opt_curr
    iterations += 1

  print("For state Productive, the optimal value =", prod_opt_curr, ", the optimal policy =", prod_opt_policy)
  print("For state Exhausted, the optimal value =", exh_opt_curr, ", the optimal policy =", exh_opt_policy)
  print("For state Fit, the optimal value =", fit_opt_curr, ", the optimal policy =", fit_opt_policy)
  #print("iterations", iterations)

def state_opt_curr(state_actions, iterations, discount, prod_opt_prev, exh_opt_prev, fit_opt_prev):
  max_val = 0
  for key in state_actions.keys():
    val = 0
    counter = 0
    i = 0
    while i < len(state_actions[key]):
      if state_actions[key][i] == "productive":
        val += state_actions[key][i+1] * (state_actions[key][i+2] + (discount  * prod_opt_prev)) #or do discount ** iterations * prod_opt_prev if you need to do gamma^iterations
      elif state_actions[key][i] == "exhausted":
        val += state_actions[key][i+1] * (state_actions[key][i+2] + (discount * exh_opt_prev))
      elif state_actions[key][i] == "fit":
        val += state_actions[key][i+1] * (state_actions[key][i+2] + (discount * fit_opt_prev))

      i += 3
    #print("val", val)

    if val > max_val:
      max_val = val
      opt_policy = key
    else:
      max_val = max_val
    #max_val = max(max_val, val)

  return max_val, opt_policy
