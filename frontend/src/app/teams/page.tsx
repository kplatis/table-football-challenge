import TeamsGrid from '@/components/teams/TeamsGrid'
import { Center, Stack, Title } from '@mantine/core'

export default function TeamsPage() {
  return (
    <Stack gap="lg">
      <Center>
        <Title order={1}>Teams</Title>
      </Center>
      <TeamsGrid />
    </Stack>
  )
}
