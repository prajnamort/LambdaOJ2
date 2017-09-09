<template>
	<div class="content-wrapper">
		<personal-info></personal-info>
		<submit-list></submit-list>
	</div>
</template>

<script>
import { getSubmitList } from '@/api/user'
import { PersonalInfo, SubmitList } from '.'


export default {
  name: 'profile',
  components: {
    PersonalInfo,
    SubmitList
  }
}
</script>

<style lang="less">

</style>
