import GamesGrid from '@/components/games/GamesGrid'
import { Center, Stack, Title } from '@mantine/core'

export default function GamesPage() {
  return (
    <Stack gap="lg">
      <Center>
        <Title order={1}>Games</Title>
      </Center>
      <GamesGrid />
    </Stack>
  )
}
