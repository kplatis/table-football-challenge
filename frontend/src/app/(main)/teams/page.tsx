import TeamsGrid from '@/components/teams/TeamsGrid'
import { Stack, Title } from '@mantine/core'

export default function TeamsPage() {
  return (
    <Stack gap="lg">
      <Title order={1} ta="center" m="xl">
        Teams
      </Title>

      <TeamsGrid />
    </Stack>
  )
}
