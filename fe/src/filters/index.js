export function localtime(time, cFormat) {
	if (arguments.length === 0) {
    return null
  }

  const format = cFormat || '{y}-{m}-{d} {h}:{i}:{s}'
  let date
  if (typeof time === 'object') {
    date = time
  } else {
    date = new Date(time)
  }
  const formatObj = {
    y: date.getFullYear(),
    m: date.getMonth() + 1,
    d: date.getDate(),
    h: date.getHours(),
    i: date.getMinutes(),
    s: date.getSeconds(),
  }
  const time_str = format.replace(/{(y|m|d|h|i|s)+}/g, (result, key) => {
    let value = formatObj[key]
    if (result.length > 0 && value < 10) {
      value = '0' + value
    }
    return value || 0
  })
  return time_str
}

export function sampleStatus(val) {
  if (arguments.length === 0) {
    return null
  }
  let info = ""
  switch(val) {
    case 0:
      info = "Accepted"
      break
    case 1:
      info = "Wrong Answer"
      break
    case 2:
      info = "Time Limit Exceeded"
      break
    case 3:
      info = "Memory Limit Exceeded"
      break
    case 4:
      info = "Output Limit Exceeded"
      break
    case 5:
      info = "Bad Syscall"
      break
    case 6:
      info = "Run Time Error"
      break
    case 7:
      info = "Unknown Result"
      break
    default:
      break
  }
  return info
}

export function milliseconds(seconds) {
  if (arguments.length === 0) {
    return null
  }

  return (seconds * 1000).toString() + ' ms'
}

export function toFixedTwo(val) {
  if (arguments.length === 0) {
    return null
  }
  return Number(val).toFixed(2)
}

export function scoreRange(score) {
  if (arguments.length === 0) {
    return null
  }
  if(typeof score === "object") {
    return '判题未完成'
  }
  if(score === 100) {
    return 'COOL'
  } else if(score >= 80) {
    return 'FINE'
  } else if(score >=50) {
    return 'SAFE'
  } else if(score > 0) {
    return 'SAD'
  } else {
    return 'WORST'
  }
}