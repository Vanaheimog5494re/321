-- Build: 87cf15677e2e09079131b91417cb9882
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
